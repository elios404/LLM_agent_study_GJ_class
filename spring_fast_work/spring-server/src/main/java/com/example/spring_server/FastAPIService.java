package com.example.spring_server;

import java.util.Map;

import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;

import reactor.core.publisher.Mono;

@Service
public class FastAPIService {
    
    private final WebClient webClient = WebClient.create("http://localhost:8000");

    public String callFastString(){
        return webClient.get().uri("/hello").retrieve().bodyToMono(String.class).block(); // 이게 전부 뭐하는 코드임?
    }

    public String callFastApiWithPreference(String preference){
        // Mono<Map> response = webClient.post()
        //                             .uri("/run-graph")
        //                             .bodyValue(Map.of("preference", preference)) // FastAPI에게 전달, Post이기에 body로 전달
        //                             .retrieve() // 요청한 결과값을 가져옴
        //                             .bodyToMono(Map.class);

        Mono<Map> response = webClient.get().uri(uriBuilder -> uriBuilder.path("/run-graph")
                                                .queryParam("preference",preference).build())
                                            .retrieve()
                                            .bodyToMono(Map.class);

        Map<String, String> result = response.block(); // 파이썬의 클래스 부분을 String, String 으로 매핑

        return String.format("선호도 : %s \n 추천메뉴 : %s \n 메뉴 정보 : %s \n",
        result.get("user_preference"), result.get("recommended_menu"), result.get("menu_info"));
    }
}
