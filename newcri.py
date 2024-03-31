import requests
from bs4 import BeautifulSoup as bs


test_url="https://www.espncricinfo.com/series/asia-cup-2023-1388374/india-vs-pakistan-3rd-match-group-a-1388394"

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}


def player_details(team_data):
	team=dict()
	for player in team_data:
	       try:
	        data=player.find('a')
	        player_param=data.get('href')
	        player_name=player.find('span'). string 
	        player_type=player.find('p'). string 
	        team[player_name]=player_param
	       except:
	       	pass
	       #print(team)
	return team

def get_player(link):
	team1_data=[ ]
	team2_data=[ ]
	k=-1
	url=link+"/match-squads"
	response=requests.get(url, header)
	   # print(response.status_code)
	if response.status_code==200:
	        soup=bs(response.content, 'html.parser')
	        
	       
	        finder=soup.find_all('td', class_='ds-min-w-max')
	    
	        while k != len(finder)-1:
	                     k +=1
	                     k+=1
	                     team1_data.append(finder[k])
	                     k+=1
	                     team2_data.append(finder[k])
	        	
	        team1=player_details(team1_data)
	        team2=player_details(team2_data)
	        #print(team1)
	        #print(team2)
	return team1,team2


#t=get_player(test_url)

#print(t)
#print("\n")
#print(t2)



        
  