import wx
import wx.html2
class main(wx.Frame):
	def __init__(self):
		super().__init__(None, title="WebBrowser")
		url=wx.GetTextFromUser("link")
		self.webview = wx.html2.WebView.New(self)
		self.webview.LoadURL(url)
		self.Show()
app=wx.App()
w=main()
w.Show()
app.MainLoop()