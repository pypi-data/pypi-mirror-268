// Copyright (C) 2023 Roberto Rossini <roberros@uio.no>
//
// SPDX-License-Identifier: MIT

#pragma once

#include <algorithm>
#include <cstdint>
#include <filesystem>
#include <vector>

#include "hictk/hic/file_reader.hpp"

namespace hictk::hic::utils {
inline std::vector<std::uint32_t> list_resolutions(const std::filesystem::path& path, bool sorted) {
  auto resolutions = hic::internal::HiCFileReader(path.string()).header().resolutions;
  if (sorted) {
    std::sort(resolutions.begin(), resolutions.end());
  }
  return resolutions;
}
}  // namespace hictk::hic::utils
