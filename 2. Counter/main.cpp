

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int paramCounter(std::vector<std::string> &strings)
{
    // int count = 0;
    // for (auto mstring : strings)
    // {
    //     if (mstring.size() > 0 && (mstring[0] == 'a' || mstring[0] == 'A'))
    //     {
    //         count++;
    //     }
    // }

    int count = std::count_if(strings.begin(), strings.end(),
                              [](const std::string &raw)
                              { return (raw.size() > 0 && (raw[0] == 'a' || raw[0] == 'A')); });
    return count;
}

int main()
{
    auto v_case = std::vector<std::string>{
        "Asdfasdf",
        "fsad fasdf",
        "asdfsadf ",
        "",
    };

    std::cout << paramCounter(v_case) << std::endl;
};