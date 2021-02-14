
#include <iostream>
#include <zmq.hpp>
#include <string>
#include <unistd.h>
#include <cmath>
#include <vector>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;
constexpr double DEG2RAD = M_PI / 180.0;

int main() {
    zmq::context_t* context = new zmq::context_t();
    zmq::socket_t* publisher = new zmq::socket_t(*context, ZMQ_REP);

    unsigned int port = 5563;
    std::ostringstream bindDest;
    bindDest << "tcp://127.0.0.1:" << port;
    publisher->bind(bindDest.str());
    
    zmq::message_t request(0);
    bool notInterrupted = true;

    int gantry_ticks = 1024;
    int trolley_ticks = 2048;
    int hoist_ticks = 512;
    int millis = 128;

    // std::vector<double> crane_status(4);
    // crane_status[0] = DEG2RAD * (360 - gantry_ticks / 100.0);
    // crane_status[1] = trolley_ticks / 1000.0;
    // crane_status[2] = hoist_ticks / 1000.0;
    // crane_status[3] = millis;
    // for (int i=0; i<crane_status.size(); i++) {
    //     cout << "crane_status[" << i << "]: " << crane_status[i] << endl;
    // }
    json j;
    j["gantry_encoder"] = DEG2RAD * (360 - gantry_ticks / 100.0);
    j["trolley_encoder"] = trolley_ticks / 1000.0;
    j["hoist_encoder"] = hoist_ticks / 1000.0;
    j["timestamp"] = millis;
    std::string crane_status = j.dump();

    
    int counter = 0;
    
    while (notInterrupted) {
        publisher->recv(&request, 0);
        zmq::message_t crane_status_msg(crane_status.begin(), crane_status.end());
        
        char* requestDataBuffer = static_cast<char*>(request.data());
        string requestStr(requestDataBuffer, request.size());
        
        cout << "Got request: " << requestStr << endl;
        
        
        // string responseString = requestStr + " response";
        cout << "Response count: " << std::to_string(counter) << endl;
        counter++;
        
        // zmq::message_t responseMsg(responseString.size());
        // std::memcpy(responseMsg.data(), responseString.data(), responseString.size());
        auto success_send = publisher->send(crane_status_msg, zmq::send_flags::none);
        if (!success_send) {
            cout << "Sending crane status failed" << endl;
        }
        sleep(1);
    }
}


