// include headers that implement a archive in simple text format
#include <boost/archive/text_oarchive.hpp>
#include <boost/archive/text_iarchive.hpp>
#include <iostream>
#include <sstream>
#include <eigen3/Eigen/Dense>

using Eigen::Matrix;

class gps_position {
private:
    // friend std::ostream & operator<<(std::ostream &os, const gps_position &gp);
    friend class boost::serialization::access;
    // When the class Archive corresponds to an output archive, the
    // & operator is defined similar to <<.  Likewise, when the class Archive
    // is a type of input archive the & operator is defined similar to >>.
    // template<class Archive>
    // void serialize(Archive & ar, const unsigned int version) {
    //     ar & degrees;
    //     ar & minutes;
    //     ar & seconds;
    // }
    int degrees;
    int minutes;
    float seconds;
    Matrix<int, 4, 1> rect;

    template<class Archive>
    void serialize(Archive & ar, const unsigned int version);
public:
    gps_position();
    // gps_position(int d, int m, float s);
    gps_position(int d, int m, float s, Matrix<int, 4, 1> rect);
    const int gps_get_degrees() const;
    const int gps_get_minutes() const;
    const float gps_get_seconds() const;
    void serialize_to_string(std::ostringstream& ostr_s) const;
    void deserialize_from_string(const std::string& string_recv);
    void print_class_data() const;
};