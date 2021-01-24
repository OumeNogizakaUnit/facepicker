# facepicker
顔陽

# Require

face-recognation のインストール時にcmakeが必要になります。

# Install

github.com:OumeNogizakaUnit/facepicker.git

```
$ pip install git+https://github.com/OumeNogizakaUnit/facepicker
```

# Usage

``
$ facepicker --help
Usage: facepicker [OPTIONS] IMGDIR

Options:
  -s, --savedir PATH  [default: ./cut_img]
  --help              Show this message and exit.
```

IMGDIRに指定したディレクトリに存在する画像から、顔画像を切り取り、
savedirに指定したディレクトリに保存します。

IMGDIRの中にディレクトリを作成し、そのディレクトリの中に画像を配置してください。
ディレクトリ構成は以下の構成を想定します。

```
IMGDIR
├── name1
│   ├── name1_image1.jpg
│   └── name1_image2.jpg
├── name2
│   ├── name2_imgae1.jpg
│   ├── name2_image2.jpg


```

このディレクトリ構成を維持したままsavedirに保存されます。

```
SAVEDIR
├── name1
│   ├── name1_image1_face00.jpg
│   ├── name1_image1_face01.jpg
│   └── name1_image2_face00.jpg
├── name2
│   ├── name2_image2_face00.jpg


```

顔画像が見つからなかったものは無視し、複数みつかった画像については、`face00` `face01` と採番していきます。
