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
from ..DataModel import DataModel
from .Conditioning import Conditioning
from strenum import StrEnum


class CurveGroupRoleEnum(StrEnum):
    Image = 'Image'
    Litho = 'Litho'
    Splice = 'Splice'


@dataclass
class CurveDef(DataModel):
    """
    Represents a ZoneVu geosteering curve definition
    """
    curve_id: Optional[int] = None
    curve_group_id: Optional[int] = None
    role: Optional[CurveGroupRoleEnum] = None
    active: bool = False
    conditioning: Optional[Conditioning] = None

