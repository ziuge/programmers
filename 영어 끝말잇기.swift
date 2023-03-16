import Foundation

func solution(_ n:Int, _ words:[String]) -> [Int] {
    var game: [String] = []
    var answer: [Int] = []

    for i in 0..<words.count {        
        if i > 0 {
            let now = Array(words[i])
            let prev = Array(words[i - 1])
            if now[0] != prev[prev.count - 1] {
                answer.append((i % n) + 1)
                answer.append((i / n) + 1)
                break
            }
        }
        if game.contains(words[i]) {
            answer.append((i % n) + 1)
            answer.append((i / n) + 1)
            break
        } else {
            game.append(words[i])
        }
    }

    if answer.count == 0 {
        answer = [0, 0]
    }

    return answer
}
