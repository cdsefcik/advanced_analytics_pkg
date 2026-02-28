#include <pybind11/pybind11.h>
#include <pybind11/stl.h>  // Bridges Python list <-> std::vector
#include "analytics.h"

namespace py = pybind11;

PYBIND11_MODULE(advanced_analytics_pkg, m) {
    py::class_<advancedanalytics>(m, "advancedanalytics")
        .def(py::init<>())
        .def("compute_mean", &advancedanalytics::compute_mean);
}