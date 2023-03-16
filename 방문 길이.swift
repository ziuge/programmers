import Foundation

func solution(_ dirs:String) -> Int {
    let dirList = Array(dirs)
    var answer: [[Int]] = []
    var x = 0
    var y = 0
    var temp: [Int] = []

    for dir in dirList {
        temp = move(String(dir), x: x, y: y)

        if temp.suffix(2).contains(6) || temp.suffix(2).contains(-6) {

        } else {
            if answer.contains(temp) || answer.contains(temp.suffix(2) + temp.prefix(2)) {

        } else {
            answer.append(temp)
        }
            x = temp[2]
            y = temp[3]
        }

    }

    return answer.count
}

func move(_ dir: String, x: Int, y: Int) -> [Int] {
    let dx = [0, 0, -1, 1]
    let dy = [1, -1, 0, 0]
    let dirs = ["U", "D", "L", "R"]

    let index = dirs.firstIndex(of: dir)!

    return [x, y, x + dx[index], y + dy[index]]
}
