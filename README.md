## PyTorch Tutorials

## Pipenv の使い方

### 環境の準備
#### 環境変数の設定
* 以下の環境変数を追加する
* この環境変数を設定することでディレクトリにパッケージを保存する


```
PIPENV_VENV_IN_PROJECT : true
```

#### VS Code の設定
settings.json の設定に以下を追加する

```json
"python.venvPath": ".venv"
```

#### Pipenv を使った PyTorch のインストール
* 以下のページの PyTorch をインストールする
* https://download.pytorch.org/whl/nightly/cu101/torch_nightly.html

```bash
pipenv install https://download.pytorch.org/whl/nightly/cu101/torch-1.5.0.dev20200228-cp38-cp38-win_amd64.whl
```

### 初期化
プロジェクトを初期化する

```bash
pipenv --python 3
```

### 環境の再現
PipFile, Pipfile.lock から環境を再現する

```bash
pipenv install
```

### Pipenv での実行
#### Pipfile にスクリプトを登録する

* Pipfile にスクリプトを登録

```Pipfile
[scripts]
sample = "python sample.py"
```

* 実行

```bash
pipenv run sample
```

#### 直接スクリプトを実行

```bash
pipenv run python sample.py
```

### 参照
* [Windows + Python 3.6 + PipEnv + Visual Studio Code でPython開発環境 - Qiita](https://qiita.com/youkidkk/items/b6a6e39ee3a109001c75)
* [Pipenvを使ったPython開発まとめ - Qiita](https://qiita.com/y-tsutsu/items/54c10e0b2c6b565c887a)
* [Windows10 + Pipenv で PyTorch(GPU)を導入する - Qiita](https://qiita.com/Haaamaaaaa/items/69b30d1dbbfcea834a9d)