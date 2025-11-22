const Util = (function () {
    // 싱글톤 인스턴스
    let instance;

    // 인스턴스 생성 함수
    function createInstance() {
        return {
            
            parseDrinkFormat(drink) {
                if (!drink) return "선택안함";  // 기본값 설정
              
                const parts = drink.split('-');  // 'ab-c-de'를 '-'로 분리
                if (parts.length !== 3) return "선택안함";  // 형식이 맞지 않는 경우 기본값 반환
              
                // 정수 변환을 사용해 앞자리 '0' 제거
                const ab = parseInt(parts[0], 10);  // 'ab' 정수로 변환하여 앞자리 '0' 제거
                const c = parseInt(parts[1], 10);  // 'c' 정수로 변환
                const de = parseInt(parts[2], 10);  // 'de' 정수로 변환하여 앞자리 '0' 제거
              
                // 'c'의 값에 따라 '일', '개월', '년', '주' 단위 결정
                let unit;
                switch (c) {
                  case 0:
                    unit = "주";
                    break;
                  case 1:
                    unit = "달";
                    break;
                  // case 2:
                  //   unit = "년";
                  //   break;
                  default:
                    unit = "주";  // 기본값 설정
                }
              
                return `${ab}${unit}에 ${de}번`;
            },
        

        };
    }

    return {
        // 싱글톤 인스턴스를 반환
        getInstance() {
            if (!instance) {
                instance = createInstance();
            }
            return instance;
        },
    };
})();

export default Util;

// 사용 예시
// Vue 컴포넌트에서 가져오기:
// const util = Util.getInstance();
// 유효성 검사 호출: util.isNumeric("123"), util.formatPhoneNumber("1234567890")

// 혹은 Util.getInstance().isNumeric("123") 로 바로 사용 가능