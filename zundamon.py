import pyaudio
import json
import requests
import time
import io
import wave

def textToVoice(text):
    # ファイル名に用いるunix時間取得
    ut = time.time()

    # 音声合成処理
    # audio_query (音声合成用のクエリを作成するAPI)
    res1 = requests.post("http://localhost:50021/audio_query",
                         params={"text": text, "speaker": 1})
    # synthesis (音声合成するAPI)
    res2 = requests.post("http://localhost:50021/synthesis",
                         params={"speaker": 1},
                         data=json.dumps(res1.json()))

    # 音声データをメモリ上に読み込み
    audio_data = io.BytesIO(res2.content)
    
    # 音声データをWAV形式に変換して再生
    with wave.open(audio_data, 'rb') as wf:
        # PyAudioの初期化
        p = pyaudio.PyAudio()

        # ストリームを開く
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # データを読み取り、再生
        data = wf.readframes(1024)
        while data:
            stream.write(data)
            data = wf.readframes(1024)

        # ストリームを閉じる
        stream.stop_stream()
        stream.close()

        # PyAudioを閉じる
        p.terminate()
        

if __name__ == '__main__':
    textToVoice('ずんだもんなのだ')