// Copyright (C) 2023 Roberto Rossini <roberros@uio.no>
//
// SPDX-License-Identifier: MIT

#pragma once

// This file was generated automatically by CMake.

#include <string_view>

namespace hictk::config::git {

// clang-format off
[[nodiscard]] constexpr bool state_available() noexcept { return false; }
[[nodiscard]] constexpr std::string_view head_sha1() noexcept { return "unknown"; }
[[nodiscard]] constexpr bool is_dirty() noexcept { return false; }
[[nodiscard]] constexpr std::string_view author_name() noexcept { return "unknown"; }
[[nodiscard]] constexpr std::string_view author_email() noexcept { return "unknown"; }
[[nodiscard]] constexpr std::string_view commit_date() noexcept { return "unknown"; }
[[nodiscard]] constexpr std::string_view commit_subject() noexcept { return "unknown"; }
[[nodiscard]] constexpr std::string_view commit_body() noexcept { return "unknown"; }
[[nodiscard]] constexpr std::string_view describe() noexcept { return "unknown"; }
[[nodiscard]] constexpr std::string_view branch() noexcept { return "unknown"; }
[[nodiscard]] constexpr std::string_view tag() noexcept { return "unknown"; }
// clang-format on

}  // namespace hictk::config::git
