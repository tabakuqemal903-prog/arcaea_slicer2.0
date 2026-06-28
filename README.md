# Arc Slicer 2.0

Arcaea 谱面切片工具，将一首完整谱面按时间段切成多个独立片段，支持变速处理，并自动生成 songlist。

## 功能

- 拖拽谱面文件夹直接导入
- 自由添加多个切片时间段
- 支持变速（0.5x、0.75x、1.0x、1.25x、1.5x、2.0x）
- 自动切割 `.aff` 谱面和 `base.ogg` 音频
- 自动生成每个片段的 `songlist` 文件
- 生成合并的 `out/songlist`，包含所有片段，可直接导入游戏

## 使用方法

### 直接使用（推荐）

从 [Releases](../../releases) 下载 `ArcSlicer.exe`，双击运行，无需安装任何依赖。

### 从源码运行

**环境要求**
- Python 3.10+
- PyQt6
- ffmpeg（放在项目根目录下）

```bash
python -m pip install PyQt6
python app.py
```

### 打包成 exe

1. 将 `ffmpeg.exe` 放在项目根目录
2. 双击运行 `build.bat`

生成的 exe 在 `dist\ArcSlicer.exe`。

## 谱面文件夹结构

输入的谱面文件夹需包含：

```
songs/
└── your_song_id/
    ├── 2.aff
    ├── base.ogg
    └── base.jpg   （可选）
```

## 输出结构

```
out/
├── songlist              ← 合并 songlist（所有片段）
└── songs/
    ├── your_song_id_0_30000/
    │   ├── 2.aff
    │   ├── base.ogg
    │   ├── base.jpg
    │   └── songlist
    └── your_song_id_30000_60000/
        ├── 2.aff
        ├── base.ogg
        └── songlist
```

## Songlist 填写说明

展开界面中的 **Songlist** 面板，填写以下字段：

| 字段 | 说明 |
|------|------|
| Title Base | 曲目名称，片段会自动加编号（01、02…） |
| Artist | 曲师 |
| BPM | 显示 BPM（字符串，如 `180` 或 `120-180`） |
| BPM Base | 基准 BPM（数字，用于计算变速后的实际 BPM） |
| Set | 曲包 ID（留空默认 `single`） |
| Side | 0 = 光芒，1 = 纷争，2 = 消色 |
| Rating | 定数（整数） |
| Rating+ | 勾选表示 +（如 9+） |
| BG | 背景图 ID |
| Version | 版本号（如 `1.0`） |
| Chart Designer | 谱师 |
| Jacket Designer | 画师 |

难度固定为 FTR（ratingClass = 2）。

## 注意事项

- ffmpeg 不包含在源码中，需自行下载：https://ffmpeg.org/download.html
- 打包后的 exe 已内置 ffmpeg，无需额外安装
