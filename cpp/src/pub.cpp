#include "mqtt/async_client.h"
#include <iostream>

int main(int argc, char *argv[])
{
    std::cout << "Starting!" << std::endl;

    mqtt::async_client client("localhost", "");
    client.connect()->wait();

    mqtt::topic top(client, "logging", 1);
    auto tok = top.publish("Hi");
    tok->wait();

    std::cout << "End!" << std::endl;
    return 0;
}
