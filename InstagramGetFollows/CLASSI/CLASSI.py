#In questo file mettiamo tutte le classi che

#QUesta classe permette di maggare oggetti della tabella MAIL_POSTMARKAPP di utentidaseguire.eu
class MAIL_POSTMARKAPP:
    def __init__(self, ID, EMAIL, OGGETTO,MESSAGGIO):
        self.ID = ID
        self.EMAIL = EMAIL
        self.OGGETTO = OGGETTO
        self.MESSAGGIO = MESSAGGIO
        self.MESSAGGIO_TEMPLATE = """
                     <html>
            <body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0" bgcolor="#FFFFFF" >
            <table width="100%" cellpadding="10" cellspacing="0" class="backgroundTable" bgcolor="#FFFFFF" >
            <tr>
            <td valign="top" align="left">
            <table width="100%" cellpadding="0" cellspacing="0">
            <tr>
            <td>
            
            <div style="width:100% " class="c over">
            <div style=" 
                cursor: pointer;
                float: left;
                 height:35px;
                padding: 0;
             
                width: 275px;">
                    <a href="www.instatrack.eu"> <img alt="Instatrack.eu" style="margin:0;width:200px;background: #2B292B;" src="https://www.instatrack.eu/affiliati/images/logo.png"> </a>
              </div></div>
              <br>  <br>
            </td>
            </tr>
             
            <tr>
            <td bgcolor="#FFFFFF" valign="top"><br style="clear:both"><br style="clear:both"><br style="clear:both"><br style="clear:both">
            
            """+str(self.MESSAGGIO)+ """
            
            <br style="clear:both"><br style="clear:both"><br style="clear:both">
            </td>
            </tr>
             
            <tr>
            <td valign="top">
            <div style="border-top:1px solid #ddd;padding-top:17px">
            <span style="font-size:12px;color: #000;font-family:arial">
            &copy;  Instatrack di Giulio Tavella <br>
                                All rights reserved.<br> 
              P.IVA 02551040997 - C.F. TVLGLI94T21D969T <a href="https://www.iubenda.com/privacy-policy/52696025/legal">Privacy policy</a>
            </span>
            </div>
            </td>
            </tr>
            </table>
            </body>
            </html>

        
        """