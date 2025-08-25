import sys
import os

# add parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#header", "Pink Morsel Data Visualizer", timeout=4)
    assert dash_duo.find_element("#header").text == "Pink Morsel Data Visualizer"
    assert dash_duo.get_logs() == [], "browser console should contain no error"

def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element_by_id("graph", timeout=4)
    assert dash_duo.find_element("#graph")
    assert dash_duo.get_logs() == [], "browser console should contain no error"

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element_by_id("region-type", timeout=4)
    assert dash_duo.find_element("#region-type")
    assert dash_duo.get_logs() == [], "browser console should contain no error"