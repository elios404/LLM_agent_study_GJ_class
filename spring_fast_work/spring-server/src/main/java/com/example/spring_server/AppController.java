package com.example.spring_server;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;



@RestController
public class AppController {
    
    private final FastAPIService fastAPIService;

    public AppController(FastAPIService fastAPIService){
        this.fastAPIService = fastAPIService;
    }

    @GetMapping("/call-fastapi")
    public String callFastApi() {
        return fastAPIService.callFastString();
    }

    @GetMapping("/recommend")
    public String recommend(@RequestParam String preference) {
        return fastAPIService.callFastApiWithPreference(preference);
    }
    
    
}
