import Foundation
import AVFoundation
let args=CommandLine.arguments
let previous=AVURLAsset(url:URL(fileURLWithPath:args[1]))
let replacement=AVURLAsset(url:URL(fileURLWithPath:args[2]))
let target=URL(fileURLWithPath:args[3])
guard !FileManager.default.fileExists(atPath:target.path) else { fatalError("Refusing overwrite") }
let comp=AVMutableComposition()
let v=comp.addMutableTrack(withMediaType:.video,preferredTrackID:kCMPersistentTrackID_Invalid)!
let a=comp.addMutableTrack(withMediaType:.audio,preferredTrackID:kCMPersistentTrackID_Invalid)!
let segments:[(AVURLAsset,Double,Double)]=[(previous,0,35.566),(replacement,0,3.92),(previous,37.699333333333335,43.833)]
var cursor=CMTime.zero
for (asset,start,end) in segments {
 let range=CMTimeRange(start:CMTime(seconds:start,preferredTimescale:48000),duration:CMTime(seconds:end-start,preferredTimescale:48000))
 try v.insertTimeRange(range,of:asset.tracks(withMediaType:.video)[0],at:cursor)
 try a.insertTimeRange(range,of:asset.tracks(withMediaType:.audio)[0],at:cursor)
 cursor=CMTimeAdd(cursor,range.duration)
}
let videoComp=AVMutableVideoComposition()
videoComp.renderSize=CGSize(width:360,height:640)
videoComp.frameDuration=CMTime(value:1,timescale:30)
let instruction=AVMutableVideoCompositionInstruction()
instruction.timeRange=CMTimeRange(start:.zero,duration:cursor)
let layer=AVMutableVideoCompositionLayerInstruction(assetTrack:v)
layer.setTransform(previous.tracks(withMediaType:.video)[0].preferredTransform,at:.zero)
instruction.layerInstructions=[layer]
videoComp.instructions=[instruction]
let export=AVAssetExportSession(asset:comp,presetName:AVAssetExportPresetHighestQuality)!
export.videoComposition=videoComp
export.outputURL=target;export.outputFileType = .mp4;export.shouldOptimizeForNetworkUse=true
let done=DispatchSemaphore(value:0)
export.exportAsynchronously { done.signal() };done.wait()
guard export.status == .completed else { fatalError("Export failed: \(String(describing:export.error))") }
print("saved \(target.path); timeline seconds=\(CMTimeGetSeconds(cursor))")
