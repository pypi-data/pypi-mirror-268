#pragma once

#include <iostream>
#include <sstream>

#ifdef _WIN32
#include <Windows.h>
#else
#include <iostream>
#endif

class Log {
private:
	std::ostringstream buffer;
public:
	template <typename T>
	Log& operator<<(T const& val) {
		this->buffer << val;
		return *this;
	}
	~Log() {
		this->buffer << std::endl;
		std::string str = this->buffer.str();
#ifdef _WIN32
        std::wstring wide{ str.begin(), str.end() };
		OutputDebugStringW(wide.c_str());
#else
        std::cerr << str << std::flush;
#endif
	}
};