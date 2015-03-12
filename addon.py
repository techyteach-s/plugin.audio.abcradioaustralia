from xbmcswift2 import Plugin, xbmcgui

plugin = Plugin()

@plugin.route('/')
def main_menu():
    items = [
        {'label': plugin.get_string(30000), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/radio_national.pls",
         'is_playable': True},
		 
        {'label': plugin.get_string(30001), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/news_radio.pls",
         'is_playable': True},
		 
		{'label': plugin.get_string(30002), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/extra.pls",
         'is_playable': True},
		 
        {'label': plugin.get_string(30003), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/local_brisbane.pls",
         'is_playable': True},
         
        {'label': plugin.get_string(30004), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/local_canberra.pls",
         'is_playable': True},
        
        {'label': plugin.get_string(30005), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/local_sydney.pls",
         'is_playable': True},
         
        {'label': plugin.get_string(30006), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/local_perth.pls",
         'is_playable': True},
         
        {'label': plugin.get_string(30007), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/local_melbourne.pls",
         'is_playable': True},
         
        {'label': plugin.get_string(30008), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/local_adelaide.pls",
         'is_playable': True},
         
        {'label': plugin.get_string(30009), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/local_hobart.pls",
         'is_playable': True},
         
        {'label': plugin.get_string(30010), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/local_newcastle.pls",
         'is_playable': True},
         
        {'label': plugin.get_string(30011), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/local_darwin.pls",
         'is_playable': True},
         
        {'label': plugin.get_string(30012), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/classic_fm.pls",
         'is_playable': True},
         
        {'label': plugin.get_string(30013), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/classic_two.pls",
         'is_playable': True},
         
        {'label': plugin.get_string(30014), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/abc_jazz.pls",
         'is_playable': True},
         
        {'label': plugin.get_string(30015), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/grandstand.pls",
         'is_playable': True},
         
        {'label': plugin.get_string(30016), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/abc_country.pls",
         'is_playable': True},
         
        {'label': plugin.get_string(30017), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/local_goldcoast.pls",
         'is_playable': True}, 
	
		{'label': plugin.get_string(30018), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/dig_music.pls",
         'is_playable': True}, 
        
        {'label': plugin.get_string(30019), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/triplej.pls",
         'is_playable': True},  
        
        {'label': plugin.get_string(30020), 'path': "http://www.abc.net.au/res/streaming/audio/mp3/unearthed.pls",
         'is_playable': True}, 
	]

    return items

if __name__ == '__main__':
    plugin.run()
