import db 
from gui import InventoryApp

if __name__ == "__main__":
    db.create_tables()
    app = InventoryApp()
    app.mainloop()
