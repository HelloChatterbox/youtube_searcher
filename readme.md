# Youtube searcher

unofficial youtube search api

## Install

```bash
pip install youtube_searcher

```

## Usage


```python
from youtube_searcher import search_youtube

query = "Rob Zombie"
data = search_youtube(query)

"""
{'featured_channel': {'title': 'robzombie',
                      'videos': [{'length': '0:51',
                                  'length_human': '0 minutos e 51 segundos',
                                  'thumbnails': [{'height': 202,
                                                  'url': 'https://i.ytimg.com/vi/aQxaGpJNfyA/hq720.jpg?sqp=-oaymwEZCOgCEMoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLBlD-Yl_nt_hT9fBxDFhF1BOYQb7Q',
                                                  'width': 360},
                                                 {'height': 404,
                                                  'url': 'https://i.ytimg.com/vi/aQxaGpJNfyA/hq720.jpg?sqp=-oaymwEZCNAFEJQDSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLBoOvNMVcNn0ulgXbinINSZZRJ8yw',
                                                  'width': 720}],
                                  'title': 'Rob Zombie’s Three From Hell - '
                                           'Teaser Trailer',
                                  'url': 'https://www.youtube.com/watch?v=aQxaGpJNfyA',
                                  'videoId': 'aQxaGpJNfyA'},
  
				(...)

                                 {'length': '0:29',
                                  'length_human': '0 minutos e 29 segundos',
                                  'thumbnails': [{'height': 202,
                                                  'url': 'https://i.ytimg.com/vi/gGwDRAtHwow/hq720.jpg?sqp=-oaymwEZCOgCEMoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCJZvpxtz6XG7GohqfWqzOEPvmwKg',
                                                  'width': 360},
                                                 {'height': 404,
                                                  'url': 'https://i.ytimg.com/vi/gGwDRAtHwow/hq720.jpg?sqp=-oaymwEZCNAFEJQDSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLBKhD8qjakLARzNZTys0fHyTzB9uA',
                                                  'width': 720}],
                                  'title': 'Rob Zombie - Vinyl Catalog - '
                                           'Available March 30',
                                  'url': 'https://www.youtube.com/watch?v=gGwDRAtHwow',
                                  'videoId': 'gGwDRAtHwow'}]},
 'playlists': [{'playlistId': 'PL9E5EE14539AE3644',
                'title': 'rob zombie playlist',
                'url': 'https://www.youtube.com/watch?v=lxAOc4JYELc&list=PL9E5EE14539AE3644',
                'videoId': 'lxAOc4JYELc'}],
 'related_queries': [{'thumbnails': [{'height': 180,
                                      'url': 'https://lh3.googleusercontent.com/ekC4dHtXghjh-iLwA947TaD4iRJoV7DcxPKeKshRX3y1kt_6hr8skBDhCUQXCONLfjkm60dDnZdC7Qpe=w320-h180-p-k-c0x00ffffff-no-rj-mo',
                                      'width': 320}],
                      'title': 'marilyn manson',
                      'url': 'https://www.youtube.com/results?search_query=marilyn+manson&sp=Eh-SARwKCi9tLzAzaDUwMmsqDm1hcmlseW4gbWFuc29ueAE%253D'},
                    
  
				(...)

                     {'thumbnails': [{'height': 180,
                                      'url': '//i.ytimg.com/vi/-uWqiDIZJ4U/mqdefault.jpg',
                                      'width': 320}],
                      'title': 'rob zombie blacktop rolling',
                      'url': 'https://www.youtube.com/results?search_query=rob+zombie+blacktop+rolling&sp=eAE%253D'}],
 'related_videos': [{'length': '5:03',
                     'length_human': '5 minutos e 3 segundos',
                     'reason': 'Relacionado com a sua pesquisa',
                     'thumbnails': [{'height': 202,
                                     'url': 'https://i.ytimg.com/vi/5abamRO41fE/hq720.jpg?sqp=-oaymwEZCOgCEMoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLBJwXXKMfD_IQZR485izC1N0oc9Ig',
                                     'width': 360},
                                    {'height': 404,
                                     'url': 'https://i.ytimg.com/vi/5abamRO41fE/hq720.jpg?sqp=-oaymwEZCNAFEJQDSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLAdxi_yl0TJG3vugoYMNrV_smJczA',
                                     'width': 720}],
                     'title': 'Slipknot - Psychosocial [OFFICIAL VIDEO]',
                     'url': 'https://www.youtube.com/watch?v=5abamRO41fE',
                     'videoId': '5abamRO41fE'},
                   
  
				(...)

                    {'length': '4:12',
                     'length_human': '4 minutos e 12 segundos',
                     'reason': 'Relacionado com a sua pesquisa',
                     'thumbnails': [{'height': 202,
                                     'url': 'https://i.ytimg.com/vi/kgltKEKw_wA/hq720.jpg?sqp=-oaymwEZCOgCEMoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLBUEPTY7_wCJeu9NuddTuEv9-IEQg',
                                     'width': 360},
                                    {'height': 404,
                                     'url': 'https://i.ytimg.com/vi/kgltKEKw_wA/hq720.jpg?sqp=-oaymwEZCNAFEJQDSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLC5BrBbX-m7c8ecY83X6sgvXtiSbg',
                                     'width': 720}],
                     'title': 'Rob Zombie - Ging Gang Gong De Do Gong De Laga '
                              'Raga (Audio / Live)',
                     'url': 'https://www.youtube.com/watch?v=kgltKEKw_wA',
                     'videoId': 'kgltKEKw_wA'}],
 'videos': [{'length': '3:49',
             'length_human': '3 minutos e 49 segundos',
             'thumbnails': [{'height': 202,
                             'url': 'https://i.ytimg.com/vi/EqQuihD0hoI/hq720.jpg?sqp=-oaymwEZCOgCEMoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCm8RcNcTePxiGFrq2Uh3VBvmTs9g',
                             'width': 360},
                            {'height': 404,
                             'url': 'https://i.ytimg.com/vi/EqQuihD0hoI/hq720.jpg?sqp=-oaymwEZCNAFEJQDSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCZFTsF5LwedXNbjdb2LgSGyc6krA',
                             'width': 720}],
             'title': 'Rob Zombie - Dragula (Official Video)',
             'url': 'https://www.youtube.com/watch?v=EqQuihD0hoI',
             'videoId': 'EqQuihD0hoI'},
           
  
				(...)

 
            {'length': '2:18',
             'length_human': '2 minutos e 18 segundos',
             'thumbnails': [{'height': 202,
                             'url': 'https://i.ytimg.com/vi/FVN6CDo02gA/hq720.jpg?sqp=-oaymwEZCOgCEMoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLD7NT2rahJijDw_auqMGFhTZ8y1Yg',
                             'width': 360},
                            {'height': 404,
                             'url': 'https://i.ytimg.com/vi/FVN6CDo02gA/hq720.jpg?sqp=-oaymwEZCNAFEJQDSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLA9pqOh8m0lhTF_vFHhEjrhnYaLNw',
                             'width': 720}],
             'title': 'Rob Zombie - Get High',
             'url': 'https://www.youtube.com/watch?v=FVN6CDo02gA',
             'videoId': 'FVN6CDo02gA'}]}
"""


```
