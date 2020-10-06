#include <fstream>
#include <iostream>
#include <sstream>
#include <zmq.hpp>
#include "gps_position.hpp"

/////////////////////////////////////////////////////////////
// gps coordinate
//
// illustrates serialization for a simple type
//
using namespace std;

// void set_zmq() {
//   socket.bind("tcp" + "://" + "*" + ":" + "5031");
// }

int main() {
    // create and open a character archive for output
    // std::ofstream ofs("filename");
    ostringstream ostr_s;
    int count_zmq = 0;

    //set the zmq part
    zmq::context_t context(1);
    zmq::socket_t socket(context, ZMQ_PUB);

    socket.bind("tcp://*:5031");

    // create class instance
    Matrix<int, 4, 1> foo;
    foo << 100, 200, 300, 400;

    // const gps_position g(35, 7, 24.567f);
    const gps_position g(35, 7, 24.567f, foo);

    // save data to archive
    

    //function which serialize class data to ostringstream
    g.serialize_to_string(ostr_s);
    // archive and stream closed when destructors are called

    //prepare the zmq msg to be sent
    while (1) {
        count_zmq++;
        if (count_zmq % 500 == 0) {
            const string& cl_data = ostr_s.str();
            // const string& cl_data = "Hey dude what's up?";
            zmq::message_t message(cl_data.size());
            std::memcpy(message.data(), cl_data.data(), cl_data.size());

            socket.send(message, 0);

            cout << "sending string: " << cl_data <<" with size: "<< cl_data.size() << endl;
            g.print_class_data();
            count_zmq = 0;
        }
    }
    
    return 0;
}