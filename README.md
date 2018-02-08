# repo_repair
修复错误提示为"error.GitError"不是一个git仓库

类似于
```
error.GitError: platform/external/vixl rev-list (u'^3da731547aa872800d4034bc0e159185a5d9c4cc', 'HEAD', '--'): fatal: 不是一个 git 仓库（或者向上递归至挂载点 /home/xxx 的任何祖先目录）
停止在文件系统边界（未设置 GIT_DISCOVERY_ACROSS_FILESYSTEM）。

```
## 使用方法

下载脚本，放入源码的同步目录(.repo的上级目录)，执行python3 repair.py

输入的name示例为 platform/external/vixl (没有空格，在终端直接双击选中Shift+Ctrl+C复制)

## 说明

默认包含的xml是 .repo/manifests/default.xml .repo/manifests/snipper/aicp.xml

根据你同步的源码自己修改
