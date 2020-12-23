#
# プロセス監視モジュール
#
import os, time, subprocess, hashlib

# デフォルトのプロセスログ保存先は /tmp/procObserver/process_{Keywords(hashed)}.log

_procLogDir = "/tmp/procObserver/"

# プロセスが生きているか確認する
def hasAlreadyExecuted(keyword: str) -> bool:
    # パスを特定し
    filePath = _getLogDirPath(keyword)

    # ファイルを開き、PID履歴を取得
    try:
        with open(filePath, "r") as f:
            loggedPIDs = [int(line) for line in f.readlines()]
    except FileNotFoundError:
        loggedPIDs = []
    
    # PID履歴から「最後に起動したプロセスのID」を取得して
    if(len(loggedPIDs) > 0):
        # プロセス生存確認
        lastPID = loggedPIDs[-1]
        return _findProcessByID(lastPID)

    return False

# プロセスIDを監視対象に登録する
def register(keyword: str):
    # パスを特定し
    filePath = _getLogDirPath(keyword)

    # PIDを書き込む
    currentPID = os.getpid()
    os.makedirs(_procLogDir, exist_ok=True)
    with open(filePath, "a") as f:
        f.write(f"{currentPID}\n")

# 識別子から保存先のディレクトリを特定
def _getLogDirPath(keyword:str) -> str:
    hashedIdentifier = hashlib.md5(keyword.encode('utf-8')).hexdigest()
    filePath = f"{_procLogDir}process_{hashedIdentifier}.log"
    return filePath

# プロセスログ保存ディレクトリを取得・変更
def getProclogDir() -> str:
    return _procLogDir

def setProclogDir(dirFullPath: str):
    if(os.path.isabs(dirFullPath)):
        # /で終わらなければ/を付加
        if(dirFullPath.endswith("/")):
            _procLogDir = dirFullPath
        else:
            _procLogDir = f"{dirFullPath}/"
    else:
        # フルパスで指定してくだしあ
        print("Warning: please set proclog path absolutely.")

# pidを指定してプロセスを探す
def _findProcessByID(pid: int) -> bool:
    result = subprocess.run(("ps", "-p", f"{pid}"), capture_output=True)
    output = result.stdout.decode("utf-8").split("\n")[1:-1]

    return len(output) > 0
