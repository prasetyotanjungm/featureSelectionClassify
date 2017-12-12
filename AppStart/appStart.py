import sys
sys.path.append('D://Bahan Belajar/SKRIPSI COY/Skripsi_road_to_jan/AppClassifOrder/controllers')
print(sys.path)

import controllers

if __name__ == "__main__":
    app = controllers.Controller()
    app.title("Own Miner")
    app.resizable(width=False,height=False)
    app.configure(background="red")
    app.mainloop()