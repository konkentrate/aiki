package org.topindustries.aiki;

import org.springframework.http.HttpEntity;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.HttpHeaders;

import org.springframework.http.HttpMethod;
import org.springframework.core.ParameterizedTypeReference;

import java.util.HashMap;
import java.util.Map;
import java.util.List;

@Controller
public class UploadController {
    private final RestTemplate restTemplate = new RestTemplate();
    private final String PYTHON_API_URL = "http://localhost:8000/process";

    @GetMapping("/upload")
    public String showUploadForm() {
        return "upload";
    }

    @PostMapping("/upload")
    public String handleTextSubmission(@RequestParam("text") String textInput, Model model) {

        // Check if the input text is null or blank
        if (textInput == null || textInput.isBlank()) {
            model.addAttribute("message", "No text submitted!");
            model.addAttribute("content", "");
            return "upload_result";
        }

        // Prepare headers
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        // Prepare JSON
        Map<String, String> request = new HashMap<>();
        request.put("text", textInput);

        HttpEntity<Map<String, String>> entity = new HttpEntity<>(request, headers);    // Create HttpEntity with headers and body

        try {
            // Send to Python Service and receive a list of AikiCard objects
            List<AikiCard> cards = restTemplate.exchange(
                    PYTHON_API_URL,
                    HttpMethod.POST,
                    entity,
                    new ParameterizedTypeReference<List<AikiCard>>() {
                    }
            ).getBody();

            // Check if cards are null or empty
            if (cards == null || cards.isEmpty()) {
                model.addAttribute("message", "No cards generated from the text!");
                model.addAttribute("content", "");
                return "upload_result";
            }
        } catch (Exception e) {
            model.addAttribute("message", "Error processing the text: " + e.getMessage());
            return "upload_result";
        }

        return textInput;

    }

}

