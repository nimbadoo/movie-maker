import Foundation
import AVFoundation
let args=CommandLine.arguments
let t7=AVURLAsset(url:URL(fileURLWithPath:args[1]))
let t8=AVURLAsset(url:URL(fileURLWithPath:args[2]))
let composition=AVMutableComposition()
let v=composition.addMutableTrack(withMediaType:.video,preferredTrackID:kCMPersistentTrackID_Invalid)!
let a7=composition.addMutableTrack(withMediaType:.audio,preferredTrackID:kCMPersistentTrackID_Invalid)!
let a8=composition.addMutableTrack(withMediaType:.audio,preferredTrackID:kCMPersistentTrackID_Invalid)!
let ranges:[(AVURLAsset,Double,Double,AVMutableCompositionTrack)]=[(t7,1.0,2.43,a7),(t8,2.43,3.16,a8),(t8,3.99,5.75,a8)]
var cursor=CMTime.zero
for (asset,start,end,a) in ranges {
 let range=CMTimeRange(start:CMTime(seconds:start,preferredTimescale:48000),duration:CMTime(seconds:end-start,preferredTimescale:48000))
 try v.insertTimeRange(range,of:asset.tracks(withMediaType:.video)[0],at:cursor)
 try a.insertTimeRange(range,of:asset.tracks(withMediaType:.audio)[0],at:cursor)
 cursor=CMTimeAdd(cursor,range.duration)
}
v.preferredTransform=t7.tracks(withMediaType:.video)[0].preferredTransform
let mix=AVMutableAudioMix()
let p7=AVMutableAudioMixInputParameters(track:a7);p7.setVolume(1.0,at:.zero)
let p8=AVMutableAudioMixInputParameters(track:a8);p8.setVolume(1.20,at:.zero)
mix.inputParameters=[p7,p8]
let export=AVAssetExportSession(asset:composition,presetName:AVAssetExportPresetHighestQuality)!
export.audioMix=mix
export.outputURL=URL(fileURLWithPath:args[3])
export.outputFileType = .mp4
export.shouldOptimizeForNetworkUse=true
let done=DispatchSemaphore(value:0)
export.exportAsynchronously { done.signal() }
done.wait()
if export.status != .completed { fatalError("export \(String(describing:export.error))") }
print("candidate saved; composition seconds=\(CMTimeGetSeconds(cursor))")
