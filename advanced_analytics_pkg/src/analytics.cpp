#include "analytics.h"
#include <numeric>

double advancedanalytics::compute_mean(const std::vector<double>& data) {
    if (data.empty()) return 0.0;
    
    double sum = std::accumulate(data.begin(), data.end(), 0.0);
    return sum / static_cast<double>(data.size());
}