from NoteDB import NoteDB
from dashboard import Dashboard

#try:
# Add Your Database username and password here
db = NoteDB(username="imlegend", password="mahengandhi19@python.com")
Dashboard().initUI(db)

#except Exception as e:
 #   messagebox.showinfo("Error", "Unable to establish database connection.")