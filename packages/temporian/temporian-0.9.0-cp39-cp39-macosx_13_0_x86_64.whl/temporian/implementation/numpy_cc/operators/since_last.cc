#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>

#include <limits>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <vector>

#include "temporian/implementation/numpy_cc/operators/common.h"

namespace {
namespace py = pybind11;

py::array_t<double> since_last(const py::array_t<double> &event_timestamps,
                               const py::array_t<double> &sampling_timestamps,
                               const int steps) {
  // Input size
  const Idx n_event = event_timestamps.shape(0);
  const Idx n_sampling = sampling_timestamps.shape(0);

  // Allocate output array
  auto since_last = py::array_t<double>(n_sampling);

  // Access raw input / output data
  auto v_since_last = since_last.mutable_unchecked<1>();
  auto v_event = event_timestamps.unchecked<1>();
  auto v_sampling = sampling_timestamps.unchecked<1>();

  Idx next_event_idx = 0;
  for (Idx sampling_idx = 0; sampling_idx < n_sampling; sampling_idx++) {
    const auto t = v_sampling[sampling_idx];
    while (next_event_idx < n_event && v_event[next_event_idx] <= t) {
      next_event_idx++;
    }
    double value;
    Idx since_last_idx = next_event_idx - steps;
    if (since_last_idx < 0) {
      value = std::numeric_limits<double>::quiet_NaN();
    } else {
      value = t - v_event[since_last_idx];
    }
    v_since_last[sampling_idx] = value;
  }

  return since_last;
}

} // namespace

void init_since_last(py::module &m) {
  m.def("since_last", &since_last, "", py::arg("event_timestamps").noconvert(),
        py::arg("sampling_timestamps").noconvert(), py::arg("steps"));
}
