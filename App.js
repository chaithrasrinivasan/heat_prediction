import "./App.css";

function App() {
  return (
    <div className="app">
      {/* Navbar */}
      <div className="navbar">
        <h2>🌡 Smart Heat Climate Assistant</h2>
        <p>Current Location</p>
      </div>

      <div className="content-wrapper">
        {/* Main Dashboard */}
        <div className="dashboard">
          {/* Top Weather Cards */}
          <div className="cards">
            <div className="card">
              <h4>Current Temperature</h4>
              <h2 className="temp">--</h2>
            </div>

            <div className="card">
              <h4>Humidity</h4>
              <h2 className="humidity">--</h2>
            </div>

            <div className="card">
              <h4>Wind Speed</h4>
              <h2 className="wind">--</h2>
            </div>
          </div>

          {/* Recommendations Section */}
          <div className="card large-card">
            <h3>Recommendations</h3>
            <p className="placeholder-text">
              Recommendations will appear after backend integration
            </p>
          </div>

          {/* Heat Map Section */}
          <div className="card large-card">
            <h3>Heat Zones</h3>
            <p className="placeholder-text">
              Map will be displayed after backend integration
            </p>
          </div>

          {/* Trend Graph Section */}
          <div className="card large-card">
            <h3>Climate Trend (Next 7 Days)</h3>
            <p className="placeholder-text">
              Graph will be displayed after data integration
            </p>
          </div>
        </div>

        {/* Right Panel */}
        <div className="right-panel">
          <div className="card">
            <h3>Area Dashboard</h3>
            <p className="placeholder-text">Today's Data: --</p>
            <p className="placeholder-text">Tomorrow's Data: --</p>
            <p className="placeholder-text">Heat Risk: --</p>
          </div>

          <div className="card">
            <h3>Heat Risk</h3>
            <p className="placeholder-text">Current Risk Level: --</p>
            <p className="placeholder-text">
              Heat risk will be calculated based on temperature, humidity,
              and wind speed.
            </p>
          </div>

          <div className="card">
            <h3>🤖 AI Chatbot</h3>

            <div className="chatbox">
              <p className="placeholder-text">
                Chatbot response will appear after backend integration
              </p>

              <input type="text" placeholder="Ask something..." />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;