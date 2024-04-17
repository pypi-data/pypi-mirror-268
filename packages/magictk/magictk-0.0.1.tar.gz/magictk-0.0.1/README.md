![icon](http://git.hmtsai.cn/cxykevin/magictk-img-readme/raw/branch/master/icon.ico)
#                  magictk
### 一个模仿 [element plus](https://element-plus.org/) 的 tkinter 组件库

## 演示
<video width="420" height="240" controls="" src="/cxykevin/magictk-img-readme/raw/branch/master/2024-04-05_show.mp4">
<strong>您的浏览器不支持使用 HTML5 'video' 标签。</strong>
</video>

## 依赖
- `pywin32` (Only in `Windows`)

## 性能
测试机器：  
- Arch Linux x86_64
- Wayland + KDE Plasma
- Intel Celeron G1840 (2) @ `2.800GHz`
- Intel HD Graphics
- Memory: `11665MiB`
- htop

CPU 占用：
- 单窗口约 `20%`
> 非最新数据

Memory 占用：
- 约 `50 MiB`

> 性能测试会消耗 `200` MiB 内存, Tim Sort `sort()` 1e7 随机数据 测试

## 组件
> 以下组件按完成时间从上(早)到下(晚)排序
1. `Window`
  > 在 Linux 下存在强制置顶问题，且最大化存在问题
  > OSX 未经过测试
2. `Button`
3. `ProgressBar`
4. `CheckBox` (`Radio`)
  > `Radio` 可以使用 `Checkbox` 指定 `RadioGroup` 实现
5. `Menu`
6. `Select`
7. `Frame`
  > 所有组件必须配合自定义的 `Frame` 使用，因为 `Frame` 携带 `root` 信息(可手动指定)
8. `Input`
  > 在 `Linux` 下会弹出一个空窗口(如果没有这个窗口无法输入，原理尚不清楚)
---

以下为计划开发顺序：
9. `ScrollBar`
