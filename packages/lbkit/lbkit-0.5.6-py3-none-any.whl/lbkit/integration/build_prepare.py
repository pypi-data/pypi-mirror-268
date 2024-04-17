"""环境准备"""
import os
import shutil
import tarfile
from lbkit.integration.config import Config
from lbkit.integration.task import Task
from lbkit.log import Logger

log = Logger("product_prepare")


class ManifestValidateError(OSError):
    """Raised when validation manifest.yml failed."""

src_cwd = os.path.split(os.path.realpath(__file__))[0]

class BuildPrepare(Task):
    def check_manifest(self):
        """检查manifest文件是否满足schema格式描述"""
        self.load_manifest()

    def install_tools(self):
        url = self.get_manifest_config("tools/compiler/url")
        sha256 = self.get_manifest_config("tools/compiler/sha256")
        path = self.get_manifest_config("tools/compiler/path")
        compiler_path = path if path else os.path.join(self.config.tool_path, "linaro")

        need_untar = True

        # 下载工具
        tool_file = os.path.join(self.config.download_path, "gcc.tar.bz2")
        # 先检查安装路径下是否存在sha256.lock文件，如果存在且值相同的不处理
        sha256_flag = os.path.join(compiler_path, "sha256.lock")
        if os.path.isfile(sha256_flag):
            fp = open(sha256_flag, "r", encoding="utf-8")
            lock_sha256 = fp.readline()
            fp.close
            if lock_sha256 == sha256:
                log.info("%s exist, skip untar", sha256_flag)
                need_untar = False
        # 如果需要解压值url或sha256为空时异常
        if need_untar and url is None or sha256 is None:
            raise ManifestValidateError(self.config.manifest + " with error, tools.compiler.url or tools.compiler.sha256 is None")

        # 解压到tools/linaro目录
        self.download_url(url, tool_file, sha256)
        tar = tarfile.open(tool_file)
        top_dir = tar.next().name
        if (need_untar):
            log.info("Start untar %s", tool_file)
            shutil.rmtree(compiler_path, ignore_errors=True)
            os.makedirs(compiler_path, exist_ok=True)
            tar.extractall(compiler_path)
            # 加了工具的目录名生成真实的工具目录地址
        compiler_path = os.path.join(compiler_path, top_dir)
        self.modify_profile(compiler_path)
        with open(sha256_flag, "w+", encoding="utf-8") as fp:
            fp.write(sha256)
        log.info("Set strip to %s", self.config.strip)

    def modify_profile(self, compiler_path):
        host = self.get_manifest_config("tools/compiler/host")
        # 制作rootfs时需要strip镜像，所以需要单独指定stip路径
        self.config.strip = os.path.join(compiler_path, "bin", host + "-strip")
        profile = self.get_manifest_config("tools/conan/profile")
        src_profile = os.path.join(self.config.work_dir, profile)
        log.info("Copy profile %s", src_profile)
        if not os.path.isfile(src_profile):
            raise FileNotFoundError(f"profile {src_profile} not found")
        profiles_dir = os.path.expanduser("~/.conan2/profiles")
        dst_profile = os.path.join(profiles_dir, os.path.basename(profile))
        if os.path.isdir(profiles_dir):
            shutil.copyfile(src_profile, dst_profile, follow_symlinks=False)
        cmd = f"sed -i 's@^toolchain=.*@toolchain={compiler_path}@g' {dst_profile}"
        self.exec(cmd)
        cmd = f"sed -i 's@^target_host=.*@target_host={host}@g' {dst_profile}"
        self.exec(cmd)
        # 重写profile配置
        log.info("Overwrite profile to %s", dst_profile)
        self.config.profile_host = os.path.basename(dst_profile)

    def run(self):
        """任务入口"""
        self.check_manifest()
        self.install_tools()
if __name__ == "__main__":
    config = Config()
    build = BuildPrepare(config)
    build.run()