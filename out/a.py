import os
from PIL import Image
from pathlib import Path

def make_square_with_pil():
    # 支援的格式
    valid_extensions = ('.png', '.jpg', '.jpeg', '.webp', '.bmp')
    
    # 建立輸出資料夾
    output_dir = Path("output_squared")
    output_dir.mkdir(exist_ok=True)
    
    # 取得當前資料夾下的所有檔案
    files = [f for f in os.listdir('.') if f.lower().endswith(valid_extensions)]
    
    if not files:
        print("在此資料夾中找不到支援的圖片檔案。")
        return

    print(f"找到 {len(files)} 張圖片，開始處理...")

    for file_name in files:
        try:
            with Image.open(file_name) as img:
                # 轉為 RGBA 模式以確保支援透明度
                img = img.convert("RGBA")
                
                width, height = img.size
                # 計算正方形的邊長 (取寬高最大值)
                new_size = max(width, height)
                
                # 建立一個全透明的畫布 (大小為 new_size x new_size)
                # (0, 0, 0, 0) 代表黑色但完全透明
                new_img = Image.new("RGBA", (new_size, new_size), (0, 0, 0, 0))
                
                # 計算置中座標
                left = (new_size - width) // 2
                top = (new_size - height) // 2
                
                # 將原圖貼到透明畫布上
                new_img.paste(img, (left, top))
                
                # 儲存結果
                base_name = Path(file_name).stem
                output_path = output_dir / f"{base_name}.png"
                new_img.save(output_path, "PNG")
                
                print(f"成功: {file_name} -> {output_path}")
                
        except Exception as e:
            print(f"錯誤: 處理 {file_name} 時失敗 - {e}")

    print("\n所有圖片處理完成！")

if __name__ == "__main__":
    make_square_with_pil()