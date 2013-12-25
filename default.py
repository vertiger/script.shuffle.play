import xbmc
import xbmcgui
import xbmcvfs


def getfiles(input_dir):
    retList = []
    dirs, files = xbmcvfs.listdir(input_dir)
    [retList.extend(getfiles('%s/%s' % (input_dir, item))) for item in dirs]
    [retList.append('%s/%s' % (input_dir, item)) for item in files]
    return retList

def shuffleplay():

    path = xbmcgui.Dialog().browse(0, 'videos', 'video')
    if not path:
        return

    pDialog = xbmcgui.DialogProgress()
    pDialog.create('get video list')
    # remove the tailing slash - so we do not have to use validatePath in the called function
    files = getfiles(path[:-1])
    pDialog.close()
    if pDialog.iscanceled():
        return
    if not len(files):
        return

    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    playlist.clear()
    [playlist.add(url = xbmc.validatePath(item)) for item in files]
    playlist.shuffle()
    if playlist.size() <= 0:
        return

    xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(playlist)

if (__name__ == "__main__"):
    shuffleplay()
