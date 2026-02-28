#ifndef ANALYTICS_H
#define ANALYTICS_H

#include <vector>

class advancedanalytics {
public:
    advancedanalytics() = default; // Constructor
    double compute_mean(const std::vector<double>& data);
};

#endif