
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>

class Event{
    public:
        std::string name;
        std::string eventName;
        int startTime;
        int endTime;

        Event(const std::string& name, const std::string& eventName, const std::string& startTime, const std::string& endTime) {
            this->name = name;
            this->eventName = eventName;
            this->startTime = getTime(startTime);
            this->endTime = getTime(endTime);
        }

    private:
        int getTime(const std::string& time) {
            int hours, minutes;
            char colon;
            std::istringstream ss(time);
            ss >> hours >> colon >> minutes;
            return hours * 60 + minutes;
        }
};

std::string toString(int time) {
    int hours = time / 60;
    int minutes = time % 60;
    std::stringstream ss;
    ss << (hours < 10 ? "0" : "") << hours << ":" << (minutes < 10 ? "0" : "") << minutes;
    return ss.str();
}

std::string getMeetingTime(const std::vector<std::string>& events, int k) {
    // Parse events into objects for easier handling 
    std::vector<Event> eventList;
    for(const auto& event : events) {
        std::istringstream ss(event);
        std::string name, eventName, startTime, endTime;
        ss >> name >> eventName >> startTime >> endTime;
        eventList.emplace_back(name, eventName, startTime, endTime);
    }

    // Sort events by start time
    std::sort(eventList.begin(), eventList.end(), [](const Event& a, const Event& b) {
        return a.startTime < b.startTime;
    });

    // Check for potential overlapping events and handle them 
    for(size_t i=1; i<eventList.size(); i++) {
        if(eventList[i].startTime < eventList[i-1].endTime) {
            eventList[i].endTime = std::max(eventList[i].endTime, eventList[i-1].endTime);
            eventList[i-1].endTime = eventList[i].endTime;
        }
    }

    // Check if there's space before the first event
    if (!eventList.empty() && eventList[0].startTime >= k) {
        return "00:00";
    }

    // Check spaces between events
    for (size_t i = 1; i < eventList.size(); i++) {
        int gap = eventList[i].startTime - eventList[i-1].endTime;
        if (gap >= k) {
            return toString(eventList[i-1].endTime);
        }
    }

    // Check if there's space after the last event (assuming a day ends at 23:59)
    if (!eventList.empty()) {
        int endOfDay = 24 * 60 - 1; // 23:59
        int gap = endOfDay - eventList.back().endTime;
        if (gap >= k) {
            return toString(eventList.back().endTime);
        }
    }

    // No suitable gap found 
    return "-1";
}

int main() {
    int eventsCount;
    std::cin >> eventsCount;
    std::cin.ignore(); // Consume newline

    std::vector<std::string> events;
    for (int i = 0; i < eventsCount; i++) {
        std::string event;
        std::getline(std::cin, event);
        events.push_back(event);
    }

    int k;
    std::cin >> k;

    std::string result = getMeetingTime(events, k);
    std::cout << result << std::endl;

    return 0;
}
