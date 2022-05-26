## May7
* 拿掉entropy做比較
* 修改TRUST_REGION_CONSTRAINT做比較
* 可以試著修改module的內容

## May8 -- 恩衍
* 增加快速更動記錄檔案目標位置的功能
* 使用方式：
    * 打開draw.ipynb
    * 修改filename為想要的輸出檔名稱
    * 按下全部執行
    * 就可以看到對應的圖了
* 注意：
    * 圖在下次跑的時候會被覆蓋，建議跑下一個測資前先截圖，或是用其他filename跑

## May 13 
* 拿掉bias term試試看 (done)
* 改 1/d -> 1 / e^d (done)
* opc 改 ret (done)
* actor loss 的 clamp 拿掉 (done)
<!-- * 用 V(s) 跟 Q-ret 的 mse 去做update (看P.8 V^target, Appendix D有寫導出的方法) -->
* TRUNCATION_PARAMETER (done)

## May 26
* trust region constraint 拔掉
* SDN paper
* ret 改 opc
