from conans import ConanFile, CMake, tools


class ClickhouseclientConan(ConanFile):
    name = "clickhouse-cpp"
    version = "0.1"
    license = "http://www.apache.org/licenses/LICENSE-2.0"
    author = "Andrey l.a.r.p@yandex.ru"
    url = "https://github.com/artpaul/clickhouse-cpp.git"
    description = "Clickhouse C++ client"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        git = tools.Git(folder="clickhouse-cpp")
        git.clone("https://github.com/artpaul/clickhouse-cpp.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="clickhouse-cpp")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="clickhouse-cpp")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["clickhouse-cpp-lib"]