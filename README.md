# BOT For Python

## 使用說明
> 1. 本教學只適用 Android 5.0 以上手機
> 2. 該功能不適合長期使用可能影響手機壽命
> 3. 請勿使用於不正當之用途

## 版本、更新
2018.04.22
> v1.0 基本功能、已讀機跟查收回

## 使用方法：
[Termux]: https://play.google.com/store/apps/details?id=com.termux
[Termux:API]: https://play.google.com/store/apps/details?id=com.termux.api
1. 至 PLAY商店 下載 [Termux][]、[Termux:API][] 並安裝
2. 接著分別輸入以下指令(看到 y/n 都打y 不然無法使用)
  ```
  pkg install git
  ```
  ```
  pkg install python
  ```
  ```
  pip3 install --upgrade pip
  ```
  ```
  pip3 install linepy
  ```
  ```
  pip3 install linepy --upgrad
  ```
  ```
  git clone https://github.com/tommy924/LINEPYBOT
  ```
  ```
  cd LINEPYBOT
  ```
  ```
  python3 bot.py
  ```

3. 開啟後複製網址至LINE並登入即可使用

## 指令表
指令|說明
----|----
Help|幫助
me|發送指令者友資
mid|發送指令者MID
op:(mid)|新增使用權限
opd:(mid)|移除使用權限
Speed|查看機器速度
Set|查看設定
Reread On/Off|查看收回 打開/關閉
Delread|刪除已讀點
Setread|設定已讀點
Lookread|查詢已讀點
Tagall|標註全部人

## 參考
LINEPY 、 COCO