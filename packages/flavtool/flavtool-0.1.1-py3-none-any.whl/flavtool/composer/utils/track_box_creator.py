from flavtool.parser.boxs.container import ContainerBox
from flavtool.parser.boxs.leaf import *


class TrackBoxCreator:
    """
    TrackBox を作るクラス
    """
    def __init__(self, track_duration :int, media_time_scale : int, media_duration : int, component_subtype : str, component_name : str,
                 sample_table : ContainerBox):
        """

        Parameters
        ----------
        track_duration :int
            トラックの長さ(Movie時間における)
        media_time_scale :int
            メディアタイムスケール
        media_duration : int
            メディアの長さ(メディア時間における)
        component_subtype : str
            コンポーネントサブタイプ(tast等)
        component_name : str
            コンポーネントネーム
        sample_table : ContainerBox
            サンプルテーブル
        """
        self.track_duration = track_duration
        self.media_time_scale = media_time_scale
        self.media_duration = media_duration
        self.component_subtype = component_subtype
        self.component_name = component_name
        self.sample_table = sample_table

    def create(self) -> ContainerBox:
        """
        TrackBoxを作成
        Returns
        -------
        track_box : ContainerBox
        """
        now = (datetime.now() - datetime(1904, 1, 1)).total_seconds()
        track_box = ContainerBox(
            box_type="trak",
            children=[
                TkhdBox(
                    box_type="tkhd",
                    creation_time=int(now),
                    modification_time=int(now),
                    duration=self.track_duration,
                    layer=0,
                    volume=1.0
                ),
                ContainerBox(
                    box_type="edts",
                    children=[
                        ElstBox(
                            box_type="elst",
                            number_of_entries=1,
                            edit_list_table=[
                                EditList(
                                    track_duration=self.track_duration,
                                    media_time=0,
                                    media_rate=1.0
                                )
                            ]
                        )
                    ]
                ),
                ContainerBox(
                    box_type="mdia",
                    children=[
                        MdhdBox(
                            box_type="mdhd",
                            creation_time=int(now),
                            modification_time=int(now),
                            time_scale=self.media_time_scale,
                            duration=self.media_duration,
                            language=10766,
                        ),
                        HdlrBox(
                            box_type="hdlr",
                            component_type="mhlr",
                            component_subtype=self.component_subtype,
                            component_name=bytes(12) + self.component_name.encode("ascii")
                        ),
                        ContainerBox(
                            box_type="minf",
                            children=[
                                TmhdBox(
                                    box_type="tmhd",
                                    balance=0
                                ),
                                ContainerBox(
                                    box_type="dinf",
                                    children=[
                                        DrefBox(
                                            box_type="dref",
                                            number_of_entries=1,
                                            data_references=[
                                                UrlBox(box_type="url ")
                                            ]
                                        )
                                    ]
                                ),
                                self.sample_table
                            ]

                        )

                    ]
                )
            ]
        )
        track_box.print()
        return track_box

