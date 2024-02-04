import tkinter
import customtkinter
from pytube import YouTube

#system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def startDownload():
    try:
        ytLink = link.get()
        ytObject =YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        ytObject.streams

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(text="Download Error", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining   
    percentage_of_completion = bytes_downloaded / total_size * 100 
    per = str(int(percentage_of_completion)) 
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    #Update progress bar
    progressBar.set(float(percentage_of_completion)/100)

#app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#adding UI elements
title = customtkinter.CTkLabel(app, text="Insert a Youtube Link")
title.pack(padx=10, pady=10)

#link Input
url_var = customtkinter.StringVar()
link =customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#finished Downloading
finishLabel =customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

#progressBar
progressBar = customtkinter.CTkProgressBar(app, width=300)
progressBar.set(0)
progressBar.pack(padx=20,pady=20)

#downlod Button
download =customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=20,pady=20)

#run app
app.mainloop()



