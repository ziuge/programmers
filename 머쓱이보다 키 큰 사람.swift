import Foundation

func solution(_ array:[Int], _ height:Int) -> Int {
    
    var arr = array
    arr.append(height)
    arr.sort(by: >)
    
    return arr.firstIndex(of: height)!

}
