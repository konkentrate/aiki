package org.topindustries.aiki;

public class AikiCard {

    private String front;
    private String back;
    private String tags;

    // getters, setters, and constructors
    public AikiCard() {}

    public AikiCard(String front, String back, String tags) {
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

    public String getTags() {
        return tags;
    }

}
