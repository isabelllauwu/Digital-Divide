
#simple check to make sure page loads
def test_001_loadtitle(dash_br):
    dash_br.server_url ='http://127.0.0.1:8050'
    assert dash_br.find_element(".titleDescription").text == "A comprehensive look at the internet speeds throughout Orlando, Florida and its city districts."

#makes sure all 6 current graphs display
def test_002_check_graphs_page(dash_br):
    dash_br.server_url ='http://127.0.0.1:8050'
    dash_br.multiple_click("#graphNav.navItem", 1)
    assert dash_br.find_element("#upSpeedImg")
    assert dash_br.find_element("#downSpeedImg")
    assert dash_br.find_element("#upDownSpeedImg")
    assert dash_br.find_element("#downSpeedLineImg")
    assert dash_br.find_element("#upSpeedLineImg")
    assert dash_br.find_element("#avgSpeedLineImg")