package org.topindustries.aiki;

import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.List;

public class AikiCard {

    private String front;
    private String back;
    private List<String> tags;

    // getters, setters, and constructors
    public AikiCard() {}

    public AikiCard(String front, String back, List<String> tags) {
        this.front = front;
        this.back = back;
        this.tags = tags;
    }

    // add getters and setters
    public String getFront() {
        return front;
    }

    public String getBack() {
        return back;
    }

    public List<String> getTags() {
        return tags;
    }

    public void setFront(String front) {
        this.front = front;
    }

    public void setBack(String back) {
        this.back = back;
    }

    @JsonProperty("tags")
    public void setTags(List<String> tags) {
        this.tags = tags;
    }

}
