"""任务基础类"""
import shutil
import importlib
import os
import hashlib
import requests
import jsonschema
import json, yaml
from multiprocessing import Process
from lbkit.log import Logger
from lbkit.tools import Tools

log = Logger("product_test")

from lbkit.integration.config import Config

class ManifestValidateError(OSError):
    """Raised when validation manifest.yml failed."""

class DigestNotMatchError(OSError):
    """Raised when source and destination are the same file."""

class Task(Process):
    """任务基础类，提供run和install默认实现以及其它基础该当"""
    def __init__(self, config: Config, name: str):
        super().__init__()
        self.tools = Tools(name)
        self.config = config

    def install(self):
        """安装任务"""
        log.info("install...........")

    def exec(self, cmd: str, verbose=False, ignore_error = False, sensitive=False, log_prefix=""):
        return self.tools.exec(cmd, verbose, ignore_error, sensitive, log_prefix)

    def pipe(self, cmds: list[str], ignore_error=False, out_file = None):
        self.tools.pipe(cmds, out_file, ignore_error)

    def run(self, cmd, ignore_error=False):
        return self.tools.run(cmd, ignore_error)

    def do_hook(self, path):
        """执行任务钓子，用于定制化"""
        try:
            module = importlib.import_module(path)
        except TypeError:
            log.info("Load module(%s) failed, skip", path)
            return
        log.info(module)
        hook = module.TaskHook(self.config)
        hook.run()

    def get_manifest_config(self, key: str):
        """从manifest中读取配置"""
        with open(self.config.manifest, "r", encoding="utf-8") as fp:
            manifest = yaml.load(fp, yaml.FullLoader)
        keys = key.split("/")
        for k in keys:
            manifest = manifest.get(k, None)
            if manifest is None:
                return None
        return manifest

    @staticmethod
    def file_digest_sha256(filename):
        """计算文件的sha256值"""
        sha256 = hashlib.sha256()
        fp = open(filename, "rb")
        while True:
            data = fp.read(65536)
            if len(data) == 0:
                break
            sha256.update(data)
        fp.close()
        return sha256.hexdigest()

    def download_url(self, url, dst_file, sha256sum = None):
        """下载文件"""
        log.info("Start download %s", url)
        is_local = False
        if url.startswith("file://"):
            path = url[7:]
            shutil.copyfile(path, dst_file)
            is_local = True
        if os.path.isfile(dst_file):
            digest = self.file_digest_sha256(dst_file)
            if sha256sum is None or digest == sha256sum:
                return
            if is_local:
                raise DigestNotMatchError(f"File {dst_file} with sha256 error, need: {sha256sum}, get: {digest}")
            os.unlink(dst_file)
        verify = os.environ.get("HTTPS_VERIFY", True)
        if verify:
            response = requests.get(url, timeout=30, verify=True)
        else:
            response = requests.get(url, timeout=30)
        fp = open(dst_file, "wb")
        fp.write(response.content)
        fp.close()
        digest = self.file_digest_sha256(dst_file)
        if sha256sum is None or digest == sha256sum:
            log.info("Download %s successfully", url)
            return
        raise DigestNotMatchError(f"File {dst_file} with sha256 error, need: {sha256sum}, get: {digest}")

    def load_manifest(self):
        """加载manifest.yml并验证schema文件"""
        with open(self.config.manifest, "r", encoding="utf-8") as fp:
            manifest = yaml.load(fp, yaml.FullLoader)
        schema_version = manifest.get("schema", None)
        if schema_version is None or not isinstance(schema_version, int):
            raise ManifestValidateError("Validation manifest.yml failed, Property schema not exist.")
        # 加载schmea文件验证文件合法性
        schema_url = "https://www.litebmc.com/standards/metadata/manifest.yml/schema_v" + str(schema_version)
        # 下载schema文件
        schema_file = os.path.join(self.config.temp_path, "manifest.schema.json")
        self.download_url(schema_url, schema_file)
        with open (schema_file, "rb") as fp:
            schema = json.load(fp)
        # 验证manifest.yml是否合法
        try:
            jsonschema.validate(manifest, schema)
        except jsonschema.exceptions.ValidationError as e:
            raise ManifestValidateError("manifest validate failed") from e
        return manifest