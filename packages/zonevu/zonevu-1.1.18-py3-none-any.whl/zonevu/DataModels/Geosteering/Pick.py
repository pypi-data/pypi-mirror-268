#  Copyright (c) 2024 Ubiterra Corporation. All rights reserved.
#  #
#  This ZoneVu Python SDK software is the property of Ubiterra Corporation.
#  You shall use it only in accordance with the terms of the ZoneVu Service Agreement.
#  #
#  This software is made available on PyPI for download and use. However, it is NOT open source.
#  Unauthorized copying, modification, or distribution of this software is strictly prohibited.
#  #
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#  INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
#  PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
#  FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#  ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#
#
#

from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import config
from ..DataModel import DataModel


@dataclass
class Pick(DataModel):
    # Represents a ZoneVu geosteering interpretation pick
    tvd: Optional[float] = field(default=None, metadata=config(field_name="TVD"))
    md: float = field(default=0, metadata=config(field_name="MD"))
    vx: Optional[float] = field(default=None, metadata=config(field_name="VX"))
    target_tvt: Optional[float] = field(default=None, metadata=config(field_name="TargetTVT"))
    target_tvd: Optional[float] = field(default=None, metadata=config(field_name="TargetTVD"))
    target_elevation: Optional[float] = field(default=None, metadata=config(field_name="TargetElevation"))
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    x: Optional[float] = None
    y: Optional[float] = None
    dx: Optional[float] = field(default=None, metadata=config(field_name="DX"))
    dy: Optional[float] = field(default=None, metadata=config(field_name="DY"))
    elevation: Optional[float] = None
    block_flag: bool = False
    fault_flag: bool = False
    type_wellbore_id: int = -1
    type_curve_def_id: Optional[int] = None
