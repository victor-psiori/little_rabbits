#include "gps_position.hpp"

using namespace std;

gps_position::gps_position(){};
/*
gps_position::gps_position(int d, int m, float s) :
    degrees(d), minutes(m), seconds(s)
{}
*/
gps_position::gps_position(int d, int m, float s, Matrix<int, 4, 1> rect) :
    degrees(d), minutes(m), seconds(s), rect(rect)
{}


template<class Archive>
void gps_position::serialize(Archive & ar, const unsigned int version) {
    ar & degrees;
    ar & minutes;
    ar & seconds;
    ar & rect;
}

const int gps_position::gps_get_degrees() const {
    return degrees;
}
const int gps_position::gps_get_minutes() const {
    return minutes;
}
const float gps_position::gps_get_seconds() const {
    return seconds;
}
void gps_position::serialize_to_string(ostringstream& ostr_s) const{
    boost::archive::text_oarchive oa(ostr_s);
    // write class instance to archive
    oa << *this;
}
void gps_position::deserialize_from_string(const string& string_recv) {
    // create and open an archive for input
    std::istringstream istr_s(string_recv);
    // boost::archive::text_iarchive ia(ifs);
    boost::archive::text_iarchive ia(istr_s);
    // read class state from archive
    ia >> *this;
}
void gps_position::print_class_data() const {
    cout << "degrees: " << this->degrees
            << " minutes: " << this->minutes 
            << " seconds: " << this->seconds << endl;
}