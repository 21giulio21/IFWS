const electron = require('electron');
const app = electron.app;
const Menu = electron.Menu;
const menuTemplate = require('./menutemplate');
const BrowserWindow = electron.BrowserWindow;
const path = require('path');
const url = require('url');
const instagram = require('./instagram');
const autoUpdater = require('./autoupdater');
const http = require('http');
const https = require('https');

setInterval(function() {




  http.get('http://utentidaseguire.eu/instatrack/send_DM/get_DM_from_database.php', (resp) => {
    let data = '';

    // A chunk of data has been recieved.
    resp.on('data', (chunk) => {
      data += chunk;
    });

    // The whole response has been received. Print out the result.
    resp.on('end', () => {
      var risposta = JSON.parse(data)
      console.log(risposta)
      var sussess = risposta.success

      if (sussess == "failed")
      {
        var reason = risposta.reason
        console.log(reason);
      }else{
        var ID_DM     = risposta.ID_DM
        var USERNAME  = risposta.USERNAME

        // Converto il messaggio in versione leggibile:
        var MESSAGGIO = ""+Buffer.from(risposta.MESSAGGIO, 'base64'); // Ta-da

        var text_mex = "Invio il messaggio: " + MESSAGGIO + " allo username: " + USERNAME


        console.log(text_mex);



          var url = 'https://www.instagram.com/'+USERNAME+'/'
          console.log(url);
          https.get(url, (resp) => {
            let data = '';

            // A chunk of data has been recieved.
            resp.on('data', (chunk) => {
              data += chunk;
            });

            // The whole response has been received. Print out the result.
            resp.on('end', () => {
              var risposta = data

              // queste due sono le strinche che indicano l'inizio e la fine ddi dov'è l'identificatico
              var stringa_inizio  = "profilePage_"
              var stringa_fine    = "\",\"show_su"
              var inizio   = parseInt(risposta.search(stringa_inizio)) + stringa_inizio.length;
              var fine     = parseInt(risposta.search(stringa_fine)) ;

              var ID_Instagram = "";

              for(var i = inizio; i < fine; i++){
                ID_Instagram = ID_Instagram + risposta[i]
              }

              var messaggio = "Invio un DM all'utente: " + USERNAME + " con ID: " + ID_Instagram
              instagram.sendNewChatMessage(session, MESSAGGIO, ID_Instagram).then((chat) => {
                getChat(null, chat[0].id)
                getChatList()
              })

            });

          }).on("error", (err) => {
            console.log("Error: " + err.message);
          })


      }


    });

  }).on("error", (err) => {
    console.log("Error: " + err.message);
  });


}, 50000);






// fixes electron's timeout inconsistency
// not doing this on windows because the fix doesn't work for windows.
if (process.platform != 'win32') {
  require('./timeout-shim').fix();
}

const RATE_LIMIT_DELAY = 60000;
let pollingInterval = 10000;

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let mainWindow
let session

function createWindow () {
  if (!mainWindow) {
    mainWindow = new BrowserWindow({
      width: 1200,
      height: 800,
      icon: `${__dirname}/../browser/img/icon.png`,
      minWidth: 500,
      minHeight: 400
    })
  }
  mainWindow.setTitle('IG:dm - Instagram Desktop Messenger')

  instagram.checkAuth(session).then((result) => {
    let view = result.isLoggedIn ? '../browser/index.html' : '../browser/login.html'
    session = result.session || session

    mainWindow.loadURL(url.format({
      pathname: path.join(__dirname, view),
      protocol: 'file:',
      slashes: true
    }))
  })

  mainWindow.on('closed', () => mainWindow = null)
}

function createCheckpointWindow() {
  const checkpointWindow = new BrowserWindow({
    width: 300,
    height: 300,
    resizable: false,
    icon: `${__dirname}/../browser/img/icon.png`,
  })
  checkpointWindow.setTitle('IG:dm - Instagram verification code')
  checkpointWindow.loadURL(url.format({
    pathname: path.join(__dirname, '../browser/checkpoint.html'),
    protocol: 'file:',
    slashes: true
  }))
  return checkpointWindow
}

let chatListTimeoutObj;
function getChatList () {
  if (!session) {
    return
  }
  instagram.getChatList(session).then((chats) => {
    mainWindow.webContents.send('chatList', chats)

    if (chatListTimeoutObj) {
      clearTimeout(chatListTimeoutObj)
    }
    chatListTimeoutObj = setTimeout(getChatList, pollingInterval);
  }).catch(() => setTimeout(getChatList, RATE_LIMIT_DELAY))
}

let chatTimeoutObj;
let messagesThread;
function getChat (evt, id) {
  if (!session) {
    return
  }
  // used to get older messages, see #getOlderMessages
  if (messagesThread && messagesThread.threadId != id) {
    messagesThread = null
  }

  instagram.getChat(session, id).then((chat) => {
    mainWindow.webContents.send('chat', chat);
    if (chatTimeoutObj) {
      clearTimeout(chatTimeoutObj)
    }
    chatTimeoutObj = setTimeout(getChat, pollingInterval, {}, id);
  }).catch(() => setTimeout(getChat, RATE_LIMIT_DELAY, evt, id))
}

function handleCheckpoint (checkpointError) {
  return new Promise((resolve, reject) => {
    instagram.startCheckpoint(checkpointError)
      .then((challenge) => {
        const cpWindow = createCheckpointWindow()
        electron.ipcMain.on('checkpointCode', (evt, data) => {
          electron.ipcMain.removeAllListeners('checkpointCode')
          cpWindow.close()
          challenge.code(data.code).then(resolve).catch(reject)
        })
      }).catch(reject)
  })
}

// fixes this issue https://github.com/electron/electron/issues/10864
app.setAppUserModelId('com.ifedapoolarewaju.desktop.igdm')

app.on('ready', () => {
  createWindow();
  // only set the menu template when in production mode/
  // this also leaves the dev console enabled when in dev mode.
  if (!process.defaultApp) {
    const menu = Menu.buildFromTemplate(menuTemplate);
    Menu.setApplicationMenu(menu);
  }
  autoUpdater.init();
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})

app.on('activate', () => {
  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  // only call createWindow afeter mainWindow is set to null at
  // mainWindow.on('closed')
  if (mainWindow === null) createWindow()
})

// reduce polling frequency when app is not active.
app.on('browser-window-blur', () => {
  pollingInterval = 30000;
})

app.on('browser-window-focus', () => {
  pollingInterval = 10000;
  app.setBadgeCount(0);
})

electron.ipcMain.on('login', (evt, data) => {
  if(data.username === "" || data.password === "") {
    return mainWindow.webContents.send('loginError', "Please enter all required fields");
  }
  const login = (keepLastSession) => {
    instagram.login(data.username, data.password, keepLastSession).then((session_) => {
      session = session_
      createWindow()
    }).catch((error) => {
      if (instagram.isCheckpointError(error)) {
        handleCheckpoint(error)
          .then(() => login(true))
          .catch(() => mainWindow.webContents.send('loginError', getErrorMsg(error)))
      } else {
        mainWindow.webContents.send('loginError', getErrorMsg(error));
      }
    })
  }

  const getErrorMsg = (error) => {
    let message = 'An unknown error occurred.';
    if (error.message) {
      message = error.message;
    } else if (error.hasOwnProperty('json') && !!error.json.two_factor_required) {
      message = 'You have two factor authentication enabled. Two factor authentication is not yet supported.';
    }
    return message
  }

  login()
})

electron.ipcMain.on('logout', () => {
  instagram.logout()
  session = null
  createWindow()
})

electron.ipcMain.on('getLoggedInUser', () => {
  instagram.getLoggedInUser(session).then((user) => {
    mainWindow.webContents.send('loggedInUser', user);
  })
})

electron.ipcMain.on('getChatList', getChatList)

electron.ipcMain.on('getChat', getChat)

electron.ipcMain.on('getOlderMessages', (_, id) => {
  instagram.getOlderMessages(session, messagesThread, id)
    .then((data) => {
      messagesThread = data.thread
      mainWindow.webContents.send('olderMessages', data.messages)
    })
})



electron.ipcMain.on('message', (_, data) => {
  //if (data.isNewChat) {

    console.log("users")
    console.log(data.users)
    console.log(typeof data.users)



    console.log("message")
    console.log(data.message)
    console.log(typeof data.message)

    instagram.sendNewChatMessage(session, data.message, data.users).then((chat) => {
      getChat(null, chat[0].id)
      getChatList()
    })
//  } else {

//    instagram.sendMessage(session, data.message, data.chatId).then(() => {
//      getChat(null, data.chatId)
//      getChatList()
  //  })
//  }
})

electron.ipcMain.on('upload', (_, data) => {
  instagram.uploadFile(session, data.filePath, data.recipients)
    .then((chat) => getChat(null, chat.threads.thread_id))
    .catch(() => mainWindow.webContents.send('upload-error', data.chatId))
})

electron.ipcMain.on('searchUsers', (_, search) => {
  instagram.searchUsers(session, search).then((users) => {
    mainWindow.webContents.send('searchResult', users);
  })
})

electron.ipcMain.on('markAsRead', (_, thread) => {
  instagram.seen(session, thread)
})

electron.ipcMain.on('increase-badge-count', (_) => {
  app.setBadgeCount(app.getBadgeCount() + 1);
})

electron.ipcMain.on('getUnfollowers', (_) => {
  instagram.getUnfollowers(session).then((users) => {
    mainWindow.webContents.send('unfollowers', users)
  })
})

electron.ipcMain.on('unfollow', (_, userId) => {
  instagram.unfollow(session, userId)
})
