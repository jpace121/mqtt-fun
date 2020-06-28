#include "mqtt/async_client.h"
#include <iostream>

class LogSub final : public mqtt::callback
{
public:
    LogSub(mqtt::async_client& client):
        _client{client}
    {
    }
private:
    mqtt::async_client& _client;

    void connected(const std::string& cause) override;
    void message_arrived(mqtt::const_message_ptr msg) override;
};

void LogSub::connected(const std::string& cause)
{
    std::cout << "Connected!" << std::endl;
    _client.subscribe("logging", 0);
}

void LogSub::message_arrived(mqtt::const_message_ptr msg)
{
    if(msg->get_topic() == "logging")
    {
        std::cout << "Hi " << msg->get_payload_str() << std::endl;
    }
}

int main(int argc, char *argv[])
{
    std::cout << "Starting!" << std::endl;

    mqtt::async_client client("localhost", "");

    LogSub callback(client);
    client.set_callback(callback);

    client.connect();

    while(true)
    {
    }

    return 0;
}
