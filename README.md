# tools

車輪の再発明上等で、自分が使いたいと思ったちょっとしたツールを作成しいく（予定）。

## ky_dir.py 

ファイルのサイズや行数とかを知りたいと思うことがあるが、dir コマンド等は結果が構造化されていないので扱いづらい。
それを解決するため、Python の Dictionary 形式（のまま）で出力するようにした。

ゆくゆくは出力内容の変更等オプションで設定できるようにしたいが、必要にになったときに開発する。

### usage

実行したいディレクトリに移動して実行する

サンプル構成
<pre>
>tree /f
sampledir_parent
│  sample.txt
│
└─sampledir_child
        sample.txt
</pre>

実行
<pre>
> ky_dir.py
</pre>

結果
<pre>
{'file_name': 'sample.txt', 'dir_name': 'C:\\sampledir_parent', 'file_size': 21, 'lines': 6}
{'file_name': 'sample.txt', 'dir_name': 'C:\\sampledir_child', 'file_size': 14, 'lines': 4}
</pre>
